Quaternion
==========

Definition
----------

A quaternion :math:`{\bf q}` is represented as a 4-tuple :math:`(a,b,c,d)`, with
basis :math:`\{1,i,j,k\}` written as

.. math::
   {\bf q} = (a,b,c,d) = a + b\ i + c\ j + d\ k.
   :label: q

The basis elements have multiplication property

.. math::
   i^2 = j^2 = k^2 = ijk = -1, \\
   ij = k,\ jk = i,\ ki = j, \\
   ji = -k,\ kj = -i,\ ik = -j.

The *Hamilton product* of two general quaternion is

.. math::
     ( & a_1, b_1, c_1, d_1)(a_2, b_2, c_2, d_2) \\
   = ( & a_1 a_2 - b_1 b_2 - c_1 c_2 - d_1 d_2,  \\
       & a_1 b_2 + b_1 a_2 + c_1 d_2 - d_1 c_2,  \\
       & a_1 c_2 - b_1 d_2 + c_1 a_2 + d_1 b_2,  \\
       & a_1 d_2 + b_1 c_2 - c_1 b_2 + d_1 a_2).
   :label: hamilton

A quaternion can be divided into a *scalar part* and a *vector part*

.. math::
   {\bf q} = (r, {\bf v}),\quad
   \textrm{with}\ r\in\mathbb{R}, {\bf v}\in\mathbb{R}^3.

We also consider scalar :math:`r` and 3-vector :math:`{\bf v}` as special forms
of quaternion

.. math::
   {\bf q}_r = (r, {\bf 0}),\quad
   {\bf q}_{\bf v} = (0, {\bf v}),

and write :math:`{\bf q}_r` and :math:`r` (:math:`{\bf q}_{\bf v}` and
:math:`{\bf v}`) interchangably in this note.

For quaternion :math:`{\bf q}` defined in :eq:`q`, its *conjugate* is

.. math::
   {\bf q}^* = a - b\ i - c\ j - d\ k,

its *norm* is

.. math::
   \|{\bf q}\| = \sqrt{{\bf q}{\bf q}^*} = \sqrt{{\bf q}^*{\bf q}} =
   \sqrt{a^2 + b^2 + c^2 + d^2},
   :label: norm

and its *reciprocal* is

.. math::
   {\bf q}^{-1}=\frac{{\bf q}^*}{\|{\bf q}\|^2},\quad
   {\bf q}{\bf q}^{-1} = {\bf q}^{-1}{\bf q} = 1.
   :label: reciprocal

Note that the multiplications in :eq:`norm` and :eq:`reciprocal` are Hamilton
product defined in :eq:`hamilton`.


Spatial Rotation
----------------

Given a unit vector :math:`\widehat{\bf u}=(u_x,u_y,u_z)` with a scalar angle
:math:`\theta`, we define quaternion

.. math::
   {\bf q} =
   \exp\left(\frac{\theta}{2}(u_x{\bf i}+u_y{\bf j}+u_z{\bf k})\right) =
   \cos\left(\frac{\theta}{2}\right) +
   \sin\left(\frac{\theta}{2}(u_x{\bf i}+u_y{\bf j}+u_z{\bf k})\right)

then for any given vector :math:`{\bf p}`, its rotation across axis
:math:`\widehat{\bf u}` for angle :math:`\theta` is

.. math::
   {\bf p}' = {\bf q}{\bf p}{\bf q}^{-1},

using Hamilton product :eq:`hamilton`. Note that both :math:`{\bf q}` and
:math:`-{\bf q}` performs the same rotation.

Conversion between rotation matrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given a unit quaternion :math:`{\bf q}=(a,b,c,d)`, it can be converted to a
rotation matrix as

.. math::
   \boldsymbol{R} = \left[\begin{array}{ccc}
   1-2c^{2}-2d^{2} & 2bc-2ad & 2bd+2ac \\
   2bc+2ad & 1-2b^{2}-2d^{2} & 2cd-2ab \\
   2bd-2ac & 2cd+2ab & 1-2b^{2}-2c^{2}
   \end{array}\right]

To convert from a rotation matrix :math:`\boldsymbol{R}` to a quaternion,

.. math::
   {\bf q} = \Big(
   & \frac{1}{2}\sqrt{R_{11}+R_{22}+R_{33}+1}, \\
   & \frac{1}{2}\sqrt{R_{11}-R_{22}-R_{33}+1}\ \mbox{sign}(R_{32}-R_{23}), \\
   & \frac{1}{2}\sqrt{-R_{11}+R_{22}-R_{33}+1}\ \mbox{sign}(R_{13}-R_{31}), \\
   & \frac{1}{2}\sqrt{-R_{11}-R_{22}+R_{33}+1}\ \mbox{sign}(R_{21}-R_{12})
   \ \Big).

This conversion can be implemented with a single square root, but one needs to
take special care on numerical stability when doing so.


API References
--------------

.. automodule:: quaternion
   :members:
