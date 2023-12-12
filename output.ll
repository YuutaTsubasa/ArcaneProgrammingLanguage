; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"a" = alloca float
  store float 0x4014000000000000, float* %"a"
  %"b" = alloca i32
  %".3" = zext i8 6 to i32
  store i32 %".3", i32* %"b"
  %"c" = alloca double
  %".5" = load float, float* %"a"
  %".6" = load i32, i32* %"b"
  %".7" = sitofp i32 %".6" to float
  %".8" = fmul float %".5", %".7"
  %".9" = fpext float %".8" to double
  store double %".9", double* %"c"
  %"d" = alloca i1
  store i1 1, i1* %"d"
  %".12" = load i32, i32* %"b"
  ret i32 %".12"
}
